import React from "react";

import "./style/OneTable.scss";

export const HeaderRow: React.FC = () => {
  const daysInWeak = [
    { id:1, name:"Понеділок" },{ id:2, name:"Вівторок" },
    { id:3, name:"Середа" },{ id:4, name:"Четвер" },
    { id:5, name:"П'ятниця" },{ id:6, name:"Субота" },
    { id:7, name:"Неділя" }];
  return (
    <div className="row" >
      <p className="frsInRow"></p>
      {daysInWeak.map(item => (
        <p key={item.id} className="dayP">{item.name}</p>
      ))}
    </div>
  );
};