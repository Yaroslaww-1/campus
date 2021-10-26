import { notification } from "antd";

enum NotificationType {
  success = "success",
  warning = "warning",
  info = "info",
};

interface IProps { 
  text: string,
  type:NotificationType,
  title: string,
  duration?: number
};

export const openNotification = ({ text, type, title, duration = 3 }: IProps) => {
  if (type == NotificationType.success || type == NotificationType.warning || type == NotificationType.info) {
    notification[type]({
      message: title,
      description: text,
      duration: duration,
    });
  }
};