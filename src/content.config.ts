import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Use the file name (without folders) as the id, so posts in
// articles/wordpress/ get the same short slug they had on WordPress.
const fileId = ({ entry }: { entry: string }) => entry.replace(/\.md$/, '').split('/').pop()!;

const articles = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/articles', generateId: fileId }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    // Which track the article belongs to. "general" = language-agnostic basics,
    // "other" = a topic without its own track (Groovy, Java, SOAP UI...).
    lang: z.enum(['general', 'python', 'bash', 'powershell', 'javascript', 'other']),
    // Topics, shown as /topics/<slug>/. The first one is the main topic.
    categories: z.array(z.string()).default([]),
    level: z.enum(['beginner', 'intermediate']).default('beginner'),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    // Position in the "Never coded before?" beginner path (1, 2, 3...).
    step: z.number().int().positive().optional(),
    author: z.string().default('LearnScripting'),
    draft: z.boolean().default(false),
    // Imported from WordPress: served at the old URL /<slug>/ instead of /articles/<slug>/.
    legacy: z.boolean().default(false),
    wpId: z.number().optional(),
  }),
});

// Standalone pages imported from WordPress (About us, syllabus pages...). Served at /<slug>/.
const pages = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/pages', generateId: fileId }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    draft: z.boolean().default(false),
    legacy: z.boolean().default(true),
    wpId: z.number().optional(),
  }),
});

export const collections = { articles, pages };
