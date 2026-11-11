import rss from '@astrojs/rss';
import { site } from '../data/site';
import type { APIContext } from 'astro';

export function GET(context: APIContext) {
  return rss({
    title: site.title,
    description: site.description,
    site: context.site ?? site.url,
    items: [],
    customData: '<language>en-ca</language>',
  });
}
