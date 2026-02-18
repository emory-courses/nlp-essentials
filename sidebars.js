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
    {
      type: 'category',
      label: 'Language Models',
      items: [
        'chapters/language_models/overview',
        'chapters/language_models/n-gram-models',
        'chapters/language_models/smoothing',
        'chapters/language_models/maximum-likelihood-estimation',
        'chapters/language_models/entropy-and-perplexity',
        'chapters/language_models/homework',
      ],
    },
    {
      type: 'category',
      label: 'Vector Space Models',
      items: [
        'chapters/vector_space_models/overview',
        'chapters/vector_space_models/bag-of-words-model',
        'chapters/vector_space_models/term-weighting',
        'chapters/vector_space_models/document-similarity',
        'chapters/vector_space_models/document-classification',
        'chapters/vector_space_models/homework',
      ],
    },
    {
      type: 'category',
      label: 'Distributional Semantics',
      items: [
        'chapters/distributional_semantics/overview',
        'chapters/distributional_semantics/distributional-hypothesis',
        'chapters/distributional_semantics/word-representations',
        'chapters/distributional_semantics/latent-semantic-analysis',
        'chapters/distributional_semantics/neural-networks',
        'chapters/distributional_semantics/neural-language-models',
        'chapters/distributional_semantics/homework',
      ],
    },
    {
      type: 'category',
      label: 'Large Language Models',
      items: [
        'chapters/large_language_models/overview',
        'chapters/large_language_models/homework',
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
    {
      type: 'category',
      label: 'Team Projects',
      items: [
        'projects/team_projects/current-projects',
        'projects/team_projects/projects-2025',
        'projects/team_projects/projects-2024',
        'projects/team_projects/projects-2023',
        'projects/team_projects/projects-2022',
        'projects/team_projects/projects-2021',
        'projects/team_projects/projects-2020',
      ],
    },
    {
      type: 'category',
      label: 'Project Ideas',
      items: [
        'projects/project_ideas/current-ideas',
        'projects/project_ideas/ideas-2025',
        'projects/project_ideas/ideas-2024',
      ],
    },
  ],
};

export default sidebars;
