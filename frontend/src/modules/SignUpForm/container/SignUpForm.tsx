import { SignUp } from "../components/SignUpForm";

import { authStore } from "@pages/auth/auth.store";
import { useHistory } from "react-router";

interface FormData {
  name?: string,
  surname?: string,
  email?: string,
  password?: string,
  submit?: string,
}

export const SignUpContainer = () => {
  const history = useHistory();
  const handleSubmit = (values: FormData) => {
    authStore.signUp(JSON.stringify(values))
      .then(() => history.push(authStore.path));
  };

  return <SignUp handleSubmit={handleSubmit}/>;
};