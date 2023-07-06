load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")



def rl_algorithm_rules():
    """Loads common dependencies needed to compile the grpc library."""
    if not native.existing_rule("rules_python"):
        http_archive(
            name = "rules_python",
            sha256 = "8c15896f6686beb5c631a4459a3aa8392daccaab805ea899c9d14215074b60ef",
            strip_prefix = "rules_python-0.17.3",
            url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.17.3.tar.gz",
        )

    if not native.existing_rule("com_github_grpc_grpc"):
        git_repository(
            name = "com_github_grpc_grpc",
            remote = "https://github.com/grpc/grpc",
            tag = "v1.45.2",
        )

    if not native.existing_rule("io_bazel_rules_docker"):
        http_archive(
            name = "io_bazel_rules_docker",
            sha256 = "85ffff62a4c22a74dbd98d05da6cf40f497344b3dbf1e1ab0a37ab2a1a6ca014",
            strip_prefix = "rules_docker-0.23.0",
            urls = ["https://github.com/bazelbuild/rules_docker/releases/download/v0.23.0/rules_docker-v0.23.0.tar.gz"],
        )