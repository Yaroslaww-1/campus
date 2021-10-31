import React from "react";
import { LoginForm } from "../components/LoginForm";

import { authStore } from "@pages/auth/auth.store";
import { useHistory } from "react-router";

interface FormData {
  email?: string,
  password?: string,
}


export const LoginFormContainer = () => {
  const history = useHistory();
  const handleSubmit = (values: FormData) => {
    authStore.login(JSON.stringify(values))
      .then( () => {
        history.push(authStore.path);
      });
  };
  return <LoginForm handleSubmit={handleSubmit}/>;
};