import { notification } from "antd";

interface IProps { 
  text: string,
  type:string,
  title: string,
  duration?: number
}

enum NotificationType {
  success = "success",
  warning = "warning",
  info = "info",
}

export const openNotification = ({ text, type, title, duration = 3 }: IProps) => {
  if (type == NotificationType.success || type == NotificationType.warning || type == NotificationType.info) {
    notification[type]({
      message: title,
      description: text,
      duration: duration,
    });
  }
};