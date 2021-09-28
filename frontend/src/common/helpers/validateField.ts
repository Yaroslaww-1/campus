export const validate = (key: string, touched: {[key: string]: string}, errors: {[key: string]: string}) => {
  if (touched[key]) {
    if (errors[key]) {
      return "error";
    } else {
      return "success";
    }
  } else {
    return "";
  }
};