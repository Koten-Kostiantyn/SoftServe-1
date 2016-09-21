`my.execute_command.yml` --> run a single command on cisco routers, run `bash my.unl.sh $command` to see how to use it.   
`my.execute_template.yml` --> run all commands listed in `execute_template.txt` OR if it is set up, run only missing commands, one by one apart 	
`my.napalm.yml`	--> here we gather facts with napalm  
`my.napalmshift.yml` -->	here we push configuration with napalm  
`my.show_me.yml` --> it is variatoin of `my.execute_command.yml` but starts with `show `.
`my.unl.sh` --> Hint script, it help to run ansible playbook with shell variables
