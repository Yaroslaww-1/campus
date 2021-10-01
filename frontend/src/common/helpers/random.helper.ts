export const getRandomInt = (min: number, max: number): number => {
  return Math.floor(Math.random() * max) + min;
};

export const getRandomDate = (): Date => {
  return new Date(+(new Date()) - Math.floor(Math.random() * 10000000000));
};
