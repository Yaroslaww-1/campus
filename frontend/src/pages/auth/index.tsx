import React from "react";
import { Route } from "react-router-dom";
import { LoginForm, SignUpForm } from "../../modules";

import { AppRoute } from "@common/enums/app-route.enum";

import "./Auth.scss";

export const Auth = () => {
  return (
    <section className="auth">
      <div className="auth__content">
        <Route exact path={AppRoute.LOGIN} component={LoginForm}/>
        <Route exact path={AppRoute.SIGNUP} component={SignUpForm}/>
      </div>
    </section>
  );
};