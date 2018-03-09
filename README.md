### hadoop_practice
[Udacity Intro to Hadoop Tutorial](https://www.udacity.com/course/intro-to-hadoop-and-mapreduce--ud617)


#### Running a mapreduce job with the VM alias
You can read instructions on how to download and run the virtual machines [here](https://docs.google.com/document/d/1v0zGBZ6EHap-Smsr3x3sGGpDW-54m82kDpPKC2M6uiY/edit).

You can see the input setup example [here](https://classroom.udacity.com/courses/ud617/lessons/308873795/concepts/3095085570923), and the commands for running a job [here](https://classroom.udacity.com/courses/ud617/lessons/308873795/concepts/3093825950923).

Run mapreduce from commandline:
`hs {mapper script} {reducer script} {input_file} {output directory}`

```
hadoop jar {path to hadoop streaming jar} -mapper {mapper.py} -reducer {reducer.py} -file mapper.py  -file reducer.py -input myinput{specify input} -output joboutput{specify output director reducers will write output to}
```

Read results
`hadoop fs -cat {output directory}/part-00000 | less`

Read end of file
`hadoop fs -tail {output directory}/part-00000 | less`
