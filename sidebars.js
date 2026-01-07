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
        'chapters/getting_started/overview',
        'chapters/getting_started/syllabus',
        'chapters/getting_started/schedule',
        'chapters/getting_started/development-environment',
        'chapters/getting_started/homework',
      ],
    },
    {
      type: 'category',
      label: 'Text Processing',
      items: [
        'chapters/text_processing/overview',
        'chapters/text_processing/frequency-analysis',
        'chapters/text_processing/tokenization',
        'chapters/text_processing/lemmatization',
        'chapters/text_processing/regular-expressions',
        'chapters/text_processing/homework',
      ],
    },
  ],
  projectsSidebar: [
    {
      type: 'category',
      label: 'Activities',
      items: [
        'projects/activities/overview',
        'projects/activities/speed-dating',
        'projects/activities/team-formation',
        'projects/activities/project-pitch',
        'projects/activities/proposal-report',
        'projects/activities/live-demonstration',
        'projects/activities/final-report',
      ],
    },
  ],
};

export default sidebars;
