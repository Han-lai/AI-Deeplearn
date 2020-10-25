import tensorflow as tf

fill = tf.fill([1,3],5)
fill2 = tf.fill([2,3],2)

fill3 = tf.fill([3,3],3)


with tf.Session() as sess:
    print(sess.run(fill))
    print(sess.run(fill2))
    print(sess.run(fill3))