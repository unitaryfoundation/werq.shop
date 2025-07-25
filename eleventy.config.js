module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy("styles");
  eleventyConfig.addPassthroughCopy("image");
  eleventyConfig.addPassthroughCopy("talks/slides");
  eleventyConfig.addPassthroughCopy("static");

  eleventyConfig.addCollection("talks", (collectionApi) => {
    return collectionApi
      .getFilteredByGlob("./talks/*.md")
      .filter(item => !item.inputPath.endsWith("/index.md"));
  });

  return {
    dir: {
      includes: "layouts"
    }
  };
};
