/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */

// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  chaptersSidebar: [
    {
      type: 'category',
      label: 'Getting Started',
      items: [
        'getting_started/overview',
        'getting_started/syllabus',
        'getting_started/schedule',
        'getting_started/development-environment',
        'getting_started/homework',
      ],
    },
    {
      type: 'category',
      label: 'Text Processing',
      items: [
        'text_processing/overview',
        'text_processing/frequency-analysis',
        'text_processing/tokenization',
        'text_processing/lemmatization',
        'text_processing/regular-expressions',
        'text_processing/homework',
      ],
    },
  ],
};

export default sidebars;
