#VPR Webfaction Project Template
This stack is used by VPR to publish news apps and can be used for anything from building a blog to creating web applications.

This template assumes that your host is Webfaction and includes a good deal of VPR specific code. For a more generic template, see the [VPR App Template](http://github.com/vprnet/app-template) that was the basis for this template.

## Deploying

When new updates need to be deployed do the following:

1. `cp app/_config.py app/config.py`
2. Setup the AWS credentials in `app/config.py`
3. Run `python app/index.py build` from the project root to deploy updates

## Author
[Matt Parrilla](http://twitter.com/mattparrilla)

##Copyright and License

Copyright 2013 Vermont Public Radio

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this work except in compliance with the License.
You may obtain a copy of the License in the LICENSE file, or at:

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language
governing permissions under the License.
