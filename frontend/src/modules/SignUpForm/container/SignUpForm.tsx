import React from "react";
import { SignUp } from "../components/SignUpForm";

//import api from "@api/api.helper";

interface FormData {
  name?: string,
  surname?: string,
  email?: string,
  password?: string,
  submit?: string,
}


export const SignUpContainer = () => {
  const handleSubmit = async (values: FormData) => {
    //const endpoint = "singup";
    //const token = await api.put<FormData>(endpoint, values);
    //localStorage.setItem("accessToken", JSON.stringify(token));
    setTimeout(() => {
      alert(JSON.stringify(values, null, 2));
    }, 1000);
  };

  return <SignUp handleSubmit={handleSubmit}/>;
};