import { notification } from "antd";

interface IProps { 
  text: string,
  type:string,
  title: string,
  duration?: number
}

export const openNotification = ({ text, type, title, duration = 3 }: IProps) => {
  if (type == "success" || type == "warning" || type == "info") {
    notification[type]({
      message: title,
      description: text,
      duration: duration,
    });
  }
};