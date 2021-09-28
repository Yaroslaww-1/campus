/* eslint-disable @typescript-eslint/no-explicit-any */


type errors = {
  email?: string,
  password?: string
  phone?: string,
  confirm__password?: string,
  userfullname?: string,
  username?: string,
};

export const validate = (isAuth: boolean, values: {[key: string]: string}, errors: errors ) => {
  console.log(values);
  console.log(errors);
  const rules: any= {
    email: (value: string) => {
      if (!value) {
        errors.email = "Enter your email address";
      } else if (!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i.test(value)) {
        errors.email = "Invalid email!";
      }
    },
  
    password: (value: string) => {
      if (!value) {
        errors.password = "Enter password";
      } else if (
        !isAuth &&
          !/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{5,}$/i.test(value)
      ) {
        errors.password = "The password is too easy!";
      }
    },
  
    phone: (value: string) => {
      if (!value) {
        errors.phone = "Enter your phone";
      } else if (!/^[0-9\-+]{9,15}$/i.test(value)) {
        errors.phone = "Wrong phone number!";
      }
    },
  
    confirm__password: (value: string) => {
      if (!value) {
        errors.confirm__password = "Confirm the password";
      } else if (values.password !== value) {
        errors.confirm__password = "Password mismatch!";
      }
    },
  
    userfullname: (value: string) => {
      if (!value) {
        errors.userfullname = "Enter your name";
      }
    },
  
    username: (value: string) => {
      if (!value) {
        errors.username = "Please enter your last name";
      }
    },
  };
  
  Object.keys(values).forEach(key => rules[key] && rules[key](values[key]));
};
  
//   export default validate;