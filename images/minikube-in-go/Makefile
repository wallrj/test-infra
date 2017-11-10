# Copyright 2017 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

VERSION = 0.2

image:
	docker build --build-arg KUBERNETES_VERSION=v1.8.0 -t "gcr.io/jetstack-build-infra/minikube-in-go-v1.8.0:$(VERSION)" .
	docker build --build-arg KUBERNETES_VERSION=v1.7.0 -t "gcr.io/jetstack-build-infra/minikube-in-go-v1.7.0:$(VERSION)" .

push: image
	gcloud docker -- push "gcr.io/jetstack-build-infra/minikube-in-go-v1.8.0:$(VERSION)"
	gcloud docker -- push "gcr.io/jetstack-build-infra/minikube-in-go-v1.7.0:$(VERSION)"

.PHONY: image push
