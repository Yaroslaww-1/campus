import styles from "./styles.module.scss";

interface IProps {
  src: string;
}

export const PostImageComponent: React.FC<IProps> = ({ src }) => {

  return (
    <div className={styles.root}>
      <img src={src} className={styles.image} />
    </div>
  );
};
