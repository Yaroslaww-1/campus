/* eslint-disable @typescript-eslint/no-explicit-any */
import { Link } from "react-router-dom";
import { Form, Input, Button } from "antd";
import { 
  UserOutlined,
  MailOutlined,
  LockOutlined, 
} from "@ant-design/icons";

import { Block } from "@components/index";

interface FormData {
  name?: string,
  surname?: string,
  email?: string,
  password?: string,
  submit?: string,
}

export const SignUp = ({ handleSubmit }: any) => {
  const onFinish = (values: FormData) => {
    handleSubmit(values);
  };

  return (
    <div>
      <div className="auth__top">
        <h2>Registration</h2>
        <p>To enter the campus, you need to register</p>
      </div>
      <Block>
        <Form
          name="normal_login"
          className="login-form"
          onFinish={onFinish}
        >
          <Form.Item
            name="name"
            hasFeedback
            rules={[
              { required: true, 
                message: "Please input your name!",
              },
              {
                type: "string",
                min: 5,
              },
            ]}
          >
            <Input 
              placeholder="Your name"
              prefix={<UserOutlined className="site-form-item-icon" />} 
              size="large"
            />
          </Form.Item>
          <Form.Item
            name="surname"
            hasFeedback
            rules={[
              { required: true, 
                message: "Please input your surname!",
              },
              {
                type: "string",
                min: 5,
              },
            ]}
          >
            <Input 
              placeholder="Your surname"
              prefix={<UserOutlined className="site-form-item-icon" />} 
              size="large"
            />
          </Form.Item>
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
          <Form.Item
            name="confirm"
            dependencies={["password"]}
            hasFeedback
            rules={[
              {
                type: "string",
                min: 5,
              },
              {
                required: true,
                message: "Please confirm your password!",
              },
              ({ getFieldValue }) => ({
                validator(_, value) {
                  if (!value || getFieldValue("password") === value) {
                    return Promise.resolve();
                  }
                  return Promise.reject(new Error("The two passwords that you entered do not match!"));
                },
              }),
            ]}
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
              Register now
            </Button>
          </Form.Item>
          <Link className="auth__register-link" to="/login">
              Sign in to your account
          </Link>
        </Form>
      </Block>
    </div>
  );
};