/* eslint-disable @typescript-eslint/no-explicit-any */


import React from "react";
import { Form, Input } from "antd";
import {
  UserOutlined,
  LockOutlined,
  MailOutlined,
  PhoneOutlined,
} from "@ant-design/icons";
import { Link } from "react-router-dom";
import { Button, Block } from "@components/index";
import { validate } from "@common/helpers/validateField";

const RegisterForm: React.FC = (props: any) => {
  const {
    touched,
    errors,
    handleChange,
    handleBlur,
    handleSubmit,
    isSubmitting,
  } = props;
  return (
    <div>
      <div className="auth__top">
        <h2>Registration</h2>
        <p>To enter the campus, you need to register</p>
      </div>
      <Block className=''>
        <Form onFinish={handleSubmit} className="login-form">
          <Form.Item
            name="email"
            validateStatus={validate("email", touched, errors)}
            help={!touched.email ? "" : errors.email}
            hasFeedback
          >
            <Input
              id="email"
              prefix={<MailOutlined className="site-form-item-icon" />}
              placeholder="Е-Mail"
              size="large"
              onChange={handleChange}
              onBlur={handleBlur}
            />
          </Form.Item>
          <Form.Item
            name="userfullname"
            validateStatus={validate("userfullname", touched, errors)}
            help={!touched.userfullname ? "" : errors.userfullname}
            hasFeedback
          >
            <Input
              id="userfullname"
              prefix={<UserOutlined className="site-form-item-icon" />}
              placeholder="Your name"
              size="large"
              onChange={handleChange}
              onBlur={handleBlur}
            />
          </Form.Item>
          <Form.Item
            name="username"
            validateStatus={validate("username", touched, errors)}
            help={!touched.username ? "" : errors.username}
            hasFeedback
          >
            <Input
              id="username"
              prefix={<UserOutlined className="site-form-item-icon" />}
              placeholder="Your surname"
              size="large"
              onChange={handleChange}
              onBlur={handleBlur}
            />
          </Form.Item>
          <Form.Item
            name="phone"
            validateStatus={validate("phone", touched, errors)}
            help={!touched.phone ? "" : errors.phone}
            hasFeedback
          >
            <Input
              id="phone"
              prefix={<PhoneOutlined className="site-form-item-icon" />}
              placeholder="Your phone number"
              size="large"
              onChange={handleChange}
              onBlur={handleBlur}
            />
          </Form.Item>
          <Form.Item
            name="password"
            validateStatus={validate("password", touched, errors)}
            help={!touched.password ? "" : errors.password}
            hasFeedback
          >
            <Input
              id="password"
              prefix={<LockOutlined className="site-form-item-icon" />}
              type="password"
              placeholder="Password"
              size="large"
              onChange={handleChange}
              onBlur={handleBlur}
            />
          </Form.Item>
          <Form.Item
            name="confirm__password"
            validateStatus={validate("confirm__password", touched, errors)}
            help={!touched.confirm__password ? "" : errors.confirm__password}
            hasFeedback
          >
            <Input
              id="confirm__password"
              prefix={<LockOutlined className="site-form-item-icon" />}
              type="password"
              placeholder="Repeat password"
              size="large"
              onChange={handleChange}
              onBlur={handleBlur}
            />
          </Form.Item>
          <Form.Item>
            <Button
              disabled={isSubmitting}
              onClick={handleSubmit}
              type="primary"
              size="large"
            >
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

export default RegisterForm;