export const site = {
  name: 'Balvinder Singh',
  url: 'https://balvindersingh.com',
  title: 'Balvinder Singh - Data Engineering to LLM & AI Engineering',
  description:
    'Data engineer moving into LLM and AI engineering. I help teams build production AI systems on top of solid data foundations: RAG pipelines, evals, and LLMOps.',
  email: 'info@balvindersingh.com',
  location: 'Toronto Region, Canada',
  socials: {
    github: 'https://github.com/iAmBalvinder',
    linkedin: 'https://www.linkedin.com/in/iAmBalvinder',
  },
  nav: [
    { label: 'Home', href: '/' },
    { label: 'About', href: '/about/' },
    { label: 'Contact', href: '/contact/' },
  ],
} as const;

export type Site = typeof site;
