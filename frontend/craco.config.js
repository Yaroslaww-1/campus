// const path = require("path");

// const resolvePath = p => path.resolve(__dirname, p);

// module.exports = {
//   webpack: {
//     alias: {
// "@api": resolvePath("./src/api"),
// "@common": resolvePath("./src/common"),
// "@components": resolvePath("./src/components"),
// "@models": resolvePath("./src/models"),
// "@pages": resolvePath("./src/pages"),
//     },
//   },
// };

const CracoAlias = require("craco-alias");

module.exports = {
  plugins: [
    {
      plugin: CracoAlias,
      options: {
        source: "tsconfig",
        // baseUrl SHOULD be specified
        // plugin does not take it from tsconfig
        baseUrl: "./src",
        /* tsConfigPath should point to the file where "baseUrl" and "paths" 
           are specified*/
        tsConfigPath: "./tsconfig.paths.json",
      },
    },
  ],
};