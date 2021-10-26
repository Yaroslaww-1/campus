import { SignUp } from "../components/SignUpForm";

import { authStore } from "@pages/auth/auth.store";

interface FormData {
  name?: string,
  surname?: string,
  email?: string,
  password?: string,
  submit?: string,
}

export const SignUpContainer = () => {
  const handleSubmit = async (values: FormData) => {
    authStore.signUp(JSON.stringify(values));
    setTimeout(() => {
      alert(JSON.stringify(values, null, 2));
    }, 1000);
  };

  return <SignUp handleSubmit={handleSubmit}/>;
};