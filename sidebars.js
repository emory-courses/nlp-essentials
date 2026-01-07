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
  NLPEssentialsSidebar: [
    {
      type: 'category',
      label: 'NLP Essentials',
      items: [
        'nlp_essentials/overview',
        'nlp_essentials/syllabus',
        'nlp_essentials/schedule',
        'nlp_essentials/development-environment',
        'nlp_essentials/homework',
      ],
    },
    
  ],
};

export default sidebars;
