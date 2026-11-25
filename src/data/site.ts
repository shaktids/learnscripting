export const SITE = {
  name: 'LearnScripting',
  domain: 'learnscripting.org',
  tagline: 'Learn scripting from zero. One small script at a time.',
  description:
    'Plain-English, beginner-friendly articles on Python, Bash, PowerShell and JavaScript scripting.',
  // TODO: paste your newsletter provider's form action URL (Buttondown, ConvertKit, etc.).
  // While empty, the signup form is shown but submitting does nothing.
  newsletterAction: '',
  // Google AdSense publisher ID (also in public/ads.txt). Set to '' to turn ads off.
  adsenseClient: 'ca-pub-7856118129660697',
};

export type LangId = 'python' | 'bash' | 'powershell' | 'javascript';

export interface Language {
  id: LangId;
  name: string;
  glyph: string;
  tint: string;
  blurb: string;
  use: string;
  intro: string;
}

export const LANGUAGES: Language[] = [
  {
    id: 'python',
    name: 'Python',
    glyph: 'py',
    tint: '#7DD3FC',
    blurb: 'The friendliest first language. Clean, readable, everywhere.',
    use: 'automation, data, files',
    intro:
      'Python reads almost like English, runs on every operating system and is the most popular first language for a reason. If you are unsure where to start, start here.',
  },
  {
    id: 'bash',
    name: 'Bash',
    glyph: '$_',
    tint: '#6EE7A8',
    blurb: 'The language of the Linux and macOS terminal.',
    use: 'servers, the command line',
    intro:
      'Bash is the shell behind most Linux and macOS terminals. Learn it to move around your files, chain commands together and automate server chores.',
  },
  {
    id: 'powershell',
    name: 'PowerShell',
    glyph: 'PS',
    tint: '#93C5FD',
    blurb: 'Automate Windows: files, settings, apps and more.',
    use: 'Windows, IT tasks',
    intro:
      'PowerShell comes built into Windows. It lets you manage files, settings and programs with short commands instead of endless clicking.',
  },
  {
    id: 'javascript',
    name: 'JavaScript',
    glyph: 'js',
    tint: '#FCD34D',
    blurb: 'Make web pages interactive, right in your browser.',
    use: 'websites, browser tools',
    intro:
      'JavaScript is the language of the web. Every browser can run it, so you can start experimenting right now without installing anything.',
  },
];

export const LANG_LABEL: Record<string, string> = {
  general: 'Start here',
  python: 'Python',
  bash: 'Bash',
  powershell: 'PowerShell',
  javascript: 'JavaScript',
  other: 'Article',
};

export const LANG_TINT: Record<string, string> = {
  general: '#6EE7A8',
  other: '#C4B5FD',
  ...Object.fromEntries(LANGUAGES.map((l) => [l.id, l.tint])),
};
