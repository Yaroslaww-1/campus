import React from "react";
import { LoginForm } from "../components/LoginForm";

interface FormData {
  email?: string,
  password?: string,
}


export const LoginFormContainer = () => {
  const handleSubmit = (values: FormData) => {
    setTimeout(() => {
      alert(JSON.stringify(values, null, 2));
    }, 1000);
  };

  return <LoginForm handleSubmit={handleSubmit}/>;
};