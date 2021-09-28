import { withFormik } from "formik";

import  LoginForm  from "../components/LoginForm";
import { validate as validateFunc } from "@common/helpers/validateInput";

const LoginFormContainer = withFormik({
  enableReinitialize: true,
  mapPropsToValues: () => ({
    email: "",
    password: "",
  }),
  validate: (values: {[key: string]: string}) => {
    const errors = {};
    validateFunc(true, values, errors);
    return errors;
  },
  
  handleSubmit: (values, { setSubmitting }) => {
    setTimeout(() => {
      alert(JSON.stringify(values, null, 2));
      setSubmitting(false);
    }, 1000);
  },
  
  displayName: "LoginForm",
})(LoginForm);
  
export default LoginFormContainer;