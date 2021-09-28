import React from "react";

import "./style/OneTable.scss";

import { OneRowOfTable } from "./OneRowOfTable";
import { HeaderRow } from "./HeaderRow";

export const OneTable: React.FC = () => {
  const dataArr = [
    { id:1, time:"8:30" },{ id:2, time:"10:25" },
    { id:3, time:"12:20" },{ id:4, time:"14:15" },
    { id:5, time:"16:10" },{ id:6, time:"18:30" }];

  const tmpData = [{ id:0 },{ id:1 },{ id:2 },{ id:3 },{ id:4 },{ id:5 },{ id:6 }];

  return (
    <div className="OneTable">
      <HeaderRow/>
      {dataArr.map(item =>(
        <OneRowOfTable key={item.id} time={item.time} data={tmpData}></OneRowOfTable>
      ))}
    </div>
  );
};