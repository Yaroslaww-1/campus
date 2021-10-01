import { Post } from "@models/post.model";

import styles from "./styles.module.scss";

interface IProps {
  post: Post;
}

export const PostComponent: React.FC<IProps> = ({ post }) => {
  return (
    <div className={styles.root}>
      <p>{post.name}</p>
    </div>
  );
};
