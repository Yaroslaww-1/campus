import React from "react";
import { Route } from "react-router-dom";
import { LoginForm, RegisterForm } from "../../modules";

import "./Auth.scss";

export const Auth: React.FC = () => {
  return (
    <section className="auth">
      <div className="auth__content">
        <Route path="/login" component={LoginForm} />
        <Route exact path="/signup" component={RegisterForm} />
      </div>
    </section>
  );
};