import { Post } from "@models/post.model";
import { PostComponent } from "../post";

import styles from "./styles.module.scss";

interface IProps {
  posts: Post[];
}

export const PostsListComponent: React.FC<IProps> = ({ posts }) => {

  return (
    <div className={styles.root}>
      {posts.map(post => (
        <PostComponent
          key={post.id}
          post={post}
        />
      ))}
    </div>
  );
};
