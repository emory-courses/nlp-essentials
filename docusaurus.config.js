// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'NLP Essentials',
  tagline: 'Textbook for the "NLP Essentials" course',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://emory-courses.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/nlp-essentials/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'emory-courses', // Usually your GitHub org/user name.
  projectName: 'nlp-essentials', // Usually your repo name.

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: '/', // Serve docs at the site's root
          sidebarPath: './sidebars.js',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/emory-courses/nlp-essentials/tree/main/',
        },
        blog: false, // Disable blog
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      // image: 'img/docusaurus-social-card.jpg',
      navbar: {
        style: 'dark',
        title: 'NLP Essentials',
        logo: {
          alt: 'Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'chaptersSidebar',
            position: 'left',
            label: 'Chapters',
          },
          {
            href: 'https://github.com/emory-courses/nlp-essentials',
            label: 'GitHub',
            position: 'right',
          },
          {
            href: 'https://www.emorynlp.org/faculty/jinho-choi',
            label: 'Author',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        // links: [
        //   {
        //     title: 'Course',
        //     items: [
        //       {
        //         label: 'Syllabus',
        //         to: '/overview/syllabus',
        //       },
        //       {
        //         label: 'Schedule',
        //         to: '/overview/schedule',
        //       },
        //     ],
        //   },
        //   {
        //     title: 'Resources',
        //     items: [
        //       {
        //         label: 'GitHub Repository',
        //         href: 'https://github.com/emory-courses/nlp-essentials',
        //       },
        //       {
        //         label: 'Emory NLP',
        //         href: 'https://www.emorynlp.org/',
        //       },
        //     ],
        //   },
        // ],
        copyright: `Copyright © ${new Date().getFullYear()} All rights reserved.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
        additionalLanguages: ['python', 'bash'],
      },
    }),
};

export default config;
