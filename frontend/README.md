# Getting Started with Campus frontend

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app) with ```typescript``` template.

## Technologies explanation
### Frontend
- [React](https://reactjs.org/) - main library
- [MobX](https://mobx.js.org/the-gist-of-mobx.html) - state management. [Why do we need it](https://blog.openreplay.com/do-you-really-need-redux-pros-and-cons-of-this-state-management-library) - you can skip Redux part
- [React Router](https://reactrouter.com/web/example/basic) - navigation
- [Axios](https://www.npmjs.com/package/axios) - HTTP client for the browser
### Common
- [Typescript](https://www.typescriptlang.org/) - better than nothing :)
- [ESLint](https://www.npmjs.com/package/eslint) - code linter for code conventions
- [Husky](https://www.npmjs.com/package/husky) - automatic linter on commit

## Files structure explanation
1. Main folder is **pages/**. Here we have state, local components, containers. **Pages** == **features**.
2. Shared components (for example buttons, inputs, footer, ...) in **components/**.
3. Container = component + connection with state. Shared containers (for example 'current user icon' is icon component (located in **components/**) but with state connection (connected to auth state)). Basically main concept is described in [official react docs article](https://reactjs.org/docs/thinking-in-react.html).
4. Models returned from backend stored under **models/**.
5. **api/** contains api related stuff - axios wrapper and api endpoints encapsulation.

## Available Scripts

In the project directory, you can run:

### `yarn start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `yarn test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `yarn build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `yarn eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).
