# `ele_mental` web test

This is a sample Pelican site set up to test some next generation ideas on hosting the ele-mental web services.

### Static Web Frameworks and Pelican

In order to reduce the complexity, save money and increase security, we will be heavily leaning on Static web frameworks in the next generation of ele_mental web services. Static means that there are no databases or dynamically generated pages involved in creating the pages. This reduces the chance that things will break and helps reduce our costs.

After some research, we will be doing our initial testing on Pelican.  It's a Python based static web framework. It has the benefit of supporting WordPress templates (in theory).  This is subject to testing, but initial tests look good

### Push to S3 w/ Travis CI
Automatic push to an S3 bucket is done with Travis CI.  The AWS keys are set up within Travis to allow access to the proper S3 bucket and do not need to be shared.  
Pushing to the `master` branch on the `web_test` repository (`git push origin master`) will activate the Travis CI job and do the work of loading the content off to S3.

See [this article](http://www.gregreda.com/2015/03/26/static-site-deployments/) for more information on how this was done.

### Instructions

There will be instructions and they will go here. Basically it will show how to git clone the project and push to publish mainly for beginners. 

For now here is the [marginally useful Pelican getting started guide](http://docs.getpelican.com/en/3.1.1/getting_started.html).

The [style and templating document will come in useful](http://docs.getpelican.com/en/3.1.1/themes.html) at some point

### Todo

Almost everything but specifically:

  - [x] Push to S3 w/ Travis: It's configured on the Travis and S3 side
  - [x] Generate some test content.
  - [ ] Test migrations of existing eleweb styling
  - [ ] Test of new styling / wordpress templates
  - [ ] Can existing web directory structure be ported to keep link integrity.
  - [ ] other stuff as needed. 
