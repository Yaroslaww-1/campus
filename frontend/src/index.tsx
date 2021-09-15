import React from "react";
import { Router } from "react-router-dom";
import { createBrowserHistory } from "history";
import ReactDOM from "react-dom";

import reportWebVitals from "./reportWebVitals";

import { App } from "./App";

import "./styles/index.scss";

ReactDOM.render(
  <React.StrictMode>
    <Router history={createBrowserHistory()}>
      <App />
    </Router>
  </React.StrictMode>,
  // eslint-disable-next-line comma-dangle
  document.getElementById("root")
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
