load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")



def rl_envs_rules():
    """Loads common dependencies needed to compile the protobuf library."""
    if not native.existing_rule("rl_envs"):
        git_repository(
            name = "rl_envs",
            remote = "https://github.com/cpark90/rl_envs",
            tag = "v0.04",
        )