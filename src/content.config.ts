import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { glob } from 'astro/loaders';

const services = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/services' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    order: z.number().default(99),
    deliverables: z.array(z.string()).default([]),
    timeline: z.string().optional(),
    format: z.string().optional(),
  }),
});

const caseStudies = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/case-studies' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    publishDate: z.coerce.date(),
    client: z.string(),
    industry: z.string(),
    timeframe: z.string(),
    services: z.array(z.string()).default([]),
    stack: z.array(z.string()).default([]),
    outcomes: z
      .array(
        z.object({
          metric: z.string(),
          before: z.string().optional(),
          after: z.string(),
        }),
      )
      .default([]),
    draft: z.boolean().default(false),
  }),
});

const writing = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/writing' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    publishDate: z.coerce.date(),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
  }),
});

export const collections = { services, 'case-studies': caseStudies, writing };
