import React from "react";
import { SignUp } from "../components/SignUpForm";

interface FormData {
  name?: string,
  surname?: string,
  email?: string,
  password?: string,
  submit?: string,
}


export const SignUpContainer = () => {
  const handleSubmit = (values: FormData) => {
    setTimeout(() => {
      alert(JSON.stringify(values, null, 2));
    }, 1000);
  };

  return <SignUp handleSubmit={handleSubmit}/>;
};