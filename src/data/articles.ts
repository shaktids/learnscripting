import { getCollection, type CollectionEntry } from 'astro:content';
import { LANG_LABEL } from './site';

export type Article = CollectionEntry<'articles'>;
export type Page = CollectionEntry<'pages'>;

const visible = ({ data }: { data: { draft: boolean; pubDate: Date } }) =>
  import.meta.env.DEV || (!data.draft && data.pubDate.valueOf() <= Date.now());

/**
 * All published articles, newest first.
 * Drafts and future-dated (scheduled) articles show only in `npm run dev`.
 * A scheduled article goes live on the first build on or after its pubDate,
 * and the deploy workflow rebuilds the site every day for that reason.
 */
export async function getArticles(): Promise<Article[]> {
  const all = await getCollection('articles', visible);
  return all.sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());
}

export async function getPages(): Promise<Page[]> {
  return getCollection('pages', visible);
}

/** Articles in the beginner path, ordered by step. */
export async function getPath(): Promise<Article[]> {
  const all = await getArticles();
  return all.filter((a) => a.data.step).sort((a, b) => a.data.step! - b.data.step!);
}

export function readingMinutes(body: string | undefined): number {
  const words = (body ?? '').trim().split(/\s+/).filter(Boolean).length;
  return Math.max(1, Math.round(words / 200));
}

export function formatDate(d: Date): string {
  return d.toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' });
}

/** Imported WordPress posts keep their old URL; new articles live under /articles/. */
export function articleUrl(a: Article): string {
  return a.data.legacy ? `/${a.id}/` : `/articles/${a.id}/`;
}

export function slugify(s: string): string {
  return s
    .normalize('NFKD')
    .replace(/[^\x00-\x7F]/g, '')
    .replace(/[^a-zA-Z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .toLowerCase();
}

/** The label shown on cards: the language track, or the main topic for "other". */
export function articleLabel(a: Article): string {
  if (a.data.lang === 'other') return a.data.categories[0] ?? 'Article';
  return LANG_LABEL[a.data.lang];
}

export interface Topic {
  slug: string;
  name: string;
  articles: Article[];
}

/** Every topic (category) with its articles, most popular first. */
export async function getTopics(): Promise<Topic[]> {
  const map = new Map<string, Topic>();
  for (const a of await getArticles()) {
    for (const name of a.data.categories) {
      const slug = slugify(name);
      if (!slug) continue;
      if (!map.has(slug)) map.set(slug, { slug, name, articles: [] });
      map.get(slug)!.articles.push(a);
    }
  }
  return [...map.values()].sort((a, b) => b.articles.length - a.articles.length);
}

/** Articles per page on /articles/. */
export const PER_PAGE = 24;
