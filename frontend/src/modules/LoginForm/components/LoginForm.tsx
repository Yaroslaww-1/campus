/* eslint-disable @typescript-eslint/no-explicit-any */
import { Link } from "react-router-dom";
import { Form, Input, Button } from "antd";
import { MailOutlined, LockOutlined } from "@ant-design/icons";

import { Block } from "@components/index";

interface FormData {
  email?: string,
  password?: string,
}

export const LoginForm = (props: any) => {
  const { handleSubmit } = props;
  const onFinish = (values: FormData) => {
    handleSubmit(values);
  };

  return (
    <div>
      <div className="auth__top">
        <h2>Sign in to your account</h2>
        <p>Please sign in to your account</p>
      </div>
      <Block>
        <Form
          name="normal_login"
          className="login-form"
          onFinish={onFinish}
        >
          <Form.Item
            name="email"
            rules={[
              {
                type: "email",
                message: "The input is not valid E-mail!",
              },
              {
                required: true,
                message: "Please input your E-mail!",
              },
            ]}
            hasFeedback
          >
            <Input 
              prefix={<MailOutlined className="site-form-item-icon" />} 
              placeholder="E-mail" 
              size="large"
            />
          </Form.Item>
          <Form.Item
            name="password"
            rules={[
              { 
                required: true, 
                message: "Please input your Password!", 
              },
              {
                type: "string",
                min: 5,
              },
            ]}
            hasFeedback
          >
            <Input.Password
              prefix={<LockOutlined className="site-form-item-icon" />}
              type="password"
              placeholder="Password"
              size="large"
            />
          </Form.Item>
          <Form.Item>
            <Button type="primary" htmlType="submit" className="login-form-button" block size="large">
          Log in
            </Button>
          </Form.Item>
          <Link className="auth__register-link" to="/signup">
              Register now
          </Link>
        </Form>
      </Block>
    </div>
  );
};