import React from "react";

import { OneCell } from "./OneCell";

import "./style/OneTable.scss";

type ItemProps = {
    key: number,
    time: string,
    data: Array<{id:number}>
};

export const OneRowOfTable: React.FC<ItemProps> = ({ time, data }) => {
  return (
    <div className="row">
      <p className="frsInRow">{time}</p>
      {data.map( item => (
        <OneCell key={item.id} />
      ))}
    </div>
  );
};