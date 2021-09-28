import React from "react";

import "./style/OneTable.scss";

export const OneCell: React.FC = () => {
  return (
    <div className="tmpP">
      <h3 className="sbjName">Тест (або тиць сюди і перехід на чат предмету)</h3>
      <div className="teacherName">Іванова І.І.
        <p className="teacherFullName">Іванова Інга Іванівна</p>
      </div>
      <p className="typeOfPair">on-line</p>
      <div className="description">Опис
        <p className="pairDesk">силочка + опись якийсь, я хз який</p>
      </div>
    </div>
  );
};