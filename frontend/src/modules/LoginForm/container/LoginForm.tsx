import React from "react";
import { LoginForm } from "../components/LoginForm";

import { authStore } from "@pages/auth/auth.store";

interface FormData {
  email?: string,
  password?: string,
}


export const LoginFormContainer = () => {
  const handleSubmit = (values: FormData) => {
    authStore.login(JSON.stringify(values));
    setTimeout(() => {
      alert(JSON.stringify(values, null, 2));
    }, 1000);
  };

  return <LoginForm handleSubmit={handleSubmit}/>;
};