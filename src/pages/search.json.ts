import type { APIRoute } from 'astro';
import { articleLabel, articleUrl, getArticles } from '../data/articles';

/** A small index of every article, loaded by the search box only when someone searches. */
export const GET: APIRoute = async () => {
  const articles = await getArticles();
  const index = articles.map((a) => ({
    t: a.data.title,
    d: a.data.description,
    u: articleUrl(a),
    l: articleLabel(a),
    c: a.data.categories.join(' '),
  }));
  return new Response(JSON.stringify(index), { headers: { 'Content-Type': 'application/json' } });
};
