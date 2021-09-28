/* eslint-disable @typescript-eslint/no-explicit-any */


import React from "react";
import { Form, Input } from "antd";
import { MailOutlined, LockOutlined } from "@ant-design/icons";
import { Link } from "react-router-dom";

import { Button, Block } from "@components/index";
import { validate } from "@common/helpers/validateField";

const LoginFrom: React.FC = (props: any) => {
  const {
    values,
    touched,
    errors,
    handleChange,
    handleBlur,
    handleSubmit,
    isValid,
    isSubmitting,
  } = props;
    
  return (
    <div>
      <div className="auth__top">
        <h2>Sign in to your account</h2>
        <p>Please sign in to your account</p>
      </div>
      <Block className=''>
        <Form
          onFinish={handleSubmit}
          className="login-form"
        >
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
              value={values.email}
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
              value={values.password}
              size="large"
              onChange={handleChange}
              onBlur={handleBlur}
            />
          </Form.Item>
          <Form.Item>
            {isSubmitting && !isValid && <span>Error!</span>}
            <Button
              disabled={isSubmitting}
              onClick={handleSubmit}
              type="primary"
              size="large"
            >
                  Sign in to your account
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

export default LoginFrom;