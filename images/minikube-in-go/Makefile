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
KUBERNETES_VERSIONS = v1.8.3 v1.7.10

$(KUBERNETES_VERSIONS):
	docker build --build-arg KUBERNETES_VERSION=$@ -t "gcr.io/jetstack-build-infra/minikube-in-go-$@:$(VERSION)" .
	gcloud docker -- push "gcr.io/jetstack-build-infra/minikube-in-go-$@:$(VERSION)"

.PHONY: $(KUBERNETES_VERSIONS)
