import React from "react";
import classNames from "classnames";

import "./styles.module.scss";

export const Block: React.FC<{className?: string}> = ({ children, className }) => (
  <div className={classNames("block", className)}>{children}</div>
);