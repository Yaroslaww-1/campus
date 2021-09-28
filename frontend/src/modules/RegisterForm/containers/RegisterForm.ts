import { withFormik } from "formik";

import  RegisterForm  from "../components/RegisterForm";
import { validate as validateFunc } from "@common/helpers/validateInput";

export default withFormik({
  enableReinitialize: true,
  mapPropsToValues: () => ({
    email: "",
    password: "",
    phone: "",
    confirm__password: "",
    userfullname: "",
    username: "",
  }),
  validate: values => {
    const errors = {};
    validateFunc(false, values, errors);
    return errors;
  },

  handleSubmit: (values, { setSubmitting }) => {
    setTimeout(() => {
      alert(JSON.stringify(values, null, 2));
      setSubmitting(false);
    }, 1000);
  },

  displayName: "RegisterForm",
})(RegisterForm);